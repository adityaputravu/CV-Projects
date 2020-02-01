#include <stdio.h>
#include <malloc.h>

typedef struct Stack {
	int sp;
	int size;
	int *data;
} Stack;

Stack setupStack (int size) {
	int *data = calloc(size, sizeof(int));
	Stack stack = {0, size, data};
	return stack;
}

void destroyStack(Stack *stack) {
	if (stack->data)
		free(stack->data);
}

void push (Stack *stack, int value) {
	if (stack->sp < stack->size) {
		stack->data[stack->sp] = value;
		stack->sp++;
	}
}

void pop (Stack *stack) {
	if (stack->sp > 0)
		stack->sp--;
}

void printStack (Stack *stack) {
	for (int i = 0; i < stack->size; ++i) {
		printf("[%4d] %4d", i, stack->data[i]);
		if (stack->sp == i) 
			printf(" [  SP]");
		printf("\n");
	}
	if (stack->sp >= stack->size) 
		printf("[%4d] ---- [  SP]\n", stack->sp);
	printf("\n");
}

int main() {
	
	Stack first = setupStack(10);
	if (!first.data) 
		return -1;
	
	for (int i = 0; i < 11; ++i)	
		push(&first, 1);
	printStack(&first);

	for (int i = 0; i < 3; ++i)
		pop(&first);
	printStack(&first);
	
	push(&first, 420);
	printStack(&first);

	destroyStack(&first);

	return 0;
}


