#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct{
	struct node *prev;
	struct node *next;
	void *data;
}node;

void print_node(node *n){
	printf("Current: %8x, Prev: %8x, Next: %8x, Data: %s\n", n, n->prev, n->next, n->data);	
}

node *create_queue(void *data){
	node *head = malloc(sizeof(node)); 
	head->data = data;
	return head;
}

node *queue(node **head, void *item_data){
	node *new_head = malloc(sizeof(node));

	if(item_data)
		new_head->data = item_data;
	new_head->prev = *head;

	(*head)->next = new_head;
	*head = new_head;	
}

node *dequeue(node **head){
	node *new_head = (*head)->prev;
	new_head->next = NULL;
	
	if((*head)->data)
		free((*head)->data);
	free(*head);
	*head = new_head;
}

int main(int argc, char* argv[]){

	// Create Queue
	printf("Testing creation of queue:\n");
	printf("Queue:\n");

	char *data = malloc(10);
	strcpy(data, "Creation");
	node *my_queue = create_queue(data);
	print_node(my_queue);
	printf("\n");

	// Queue on test
	printf("Testing queuing:\n");
	printf("Queue:\n");

	char *data2 = malloc(10);
	strcpy(data2, "James");
	queue(&my_queue, data2);

	char *data3 = malloc(10);
	strcpy(data3, "Lyne");
	queue(&my_queue, data3);
	
	print_node(my_queue);
	print_node(my_queue->prev);
	print_node(((node *)(my_queue->prev))->prev);
	printf("\n");

	// Dequeue off test
	printf("Testing dequeuing:\n");
	printf("Queue:\n");
	dequeue(&my_queue);

	print_node(my_queue);
	print_node(my_queue->prev);
	printf("\n");

	return 0;
}
