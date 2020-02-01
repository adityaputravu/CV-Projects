#include <stdio.h>
#include <malloc.h>
#include <stdbool.h>

typedef struct Queue {
	bool full;
	int bp;
	int fp;
	int size;
	int *data;
} Queue;

Queue setupQueue (int size) {
	int *data = calloc(size, sizeof(int));
	Queue queue = {false, 0, 0, size, data};
	return queue;
}

void destroyQueue (Queue *queue) {
	if (queue->data)
		free(queue->data);
}

void printQueue (Queue *queue) {
	for (int i = 0; i < queue->size; ++i) {
		printf("[%4d] %4d", i, queue->data[i]);
		if (queue->bp == i)
			printf(" [  BP]");
		if (queue->fp == i)
			printf(" [  FP]");
		printf("\n");
	}
	if (queue->bp >= queue->size || queue->bp < 0)
		printf("[%4d] ---- [  BP]", queue->bp);
	if (queue->fp >= queue->size || queue->fp < 0)
		printf("[%4d] ---- [  FP]", queue->fp);
	puts("\n");	
}

void enqueue (Queue *queue, int value) {
	if (queue->full) 
		return;
	if (queue->bp + 1 == queue->fp) {
		queue->data[queue->bp] = value;
		queue->bp++;
		queue->full = true;
	}
	else if (queue->fp != 0 
	    && queue->bp - queue->fp < queue->size
	    && queue->bp == queue->size){
		queue->bp = 0;
		queue->data[queue->bp] = value;
	}
	else if (queue->bp < queue->size) {
		queue->data[queue->bp] = value;
		queue->bp++;
	}
}

int dequeue (Queue *queue) {
	int item = -1;
	if (queue->fp == queue->bp && queue->full) {
		queue->full = false;
		item = queue->fp;
		queue->fp = (queue->fp+1)%queue->size;
	}
	else if (queue->fp < queue->bp) {
		item = queue->fp;
		queue->fp++;
	}
	else if (queue->fp > queue->bp) {
		item = queue->fp;
		queue->fp = (queue->fp+1)%queue->size;
	}
	return item;
}

int main () {
	Queue first = setupQueue(10);
	if (!first.data)
		return -1;
	printf("Queue created successfully\n");


	for (int i = 0; i < 10; ++i)
		enqueue(&first, i);
	printQueue(&first);
	
	for (int i = 0; i < 5; ++i)
		dequeue(&first);
	printQueue(&first);
	
	for (int i = 0; i < 4; ++i)
		enqueue(&first, 69);
	printQueue(&first);

	for (int i = 0; i < 3; ++i)
		dequeue(&first);
	printQueue(&first);

	destroyQueue(&first);
	return 0;
}









