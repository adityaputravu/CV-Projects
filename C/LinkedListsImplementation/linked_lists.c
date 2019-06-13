#include <stdio.h>
#include <stdlib.h>

#define bool _Bool

typedef struct node{
	struct node* next;
	struct node* prev;
	int data;
}s_node;

s_node* make_list(long size, int init_val){
	/*
	 * Makes a list
	 * First node has no previous, but a next
	 * Last node has a previous, but no next
	 * 
	 * Middle nodes have both
	 *
	 * returns top of list 
	 * on memory allocation error, returns NULL
	 */

	// One liner
	// s_node* head = malloc(sizeof(*head)), *current = head; 
	s_node* head = malloc(sizeof(s_node));
	if(!head)
		return NULL;
	s_node* current = head;
	s_node* previous = NULL;

	for(int i=0; i<size; ++i){
		current->data = init_val;
		current->prev = previous;
		if(i < size-1){ // Not last node
			s_node* next = malloc(sizeof(s_node));
			if(!next)
				return NULL;
			current->next = next;
			// Update previous
			// Then update current
			previous = current;
			current = next;
		}else{		// Is last node
			current->next = NULL;
		}
	}
	
	return head;

}

void free_list(s_node* list){
	/* 
	 * Iterates through each item in list
	 * Frees the heap space allocated
	 */
	s_node* next = list;
	do{
		list = next;
		next = list->next;
		free(list);
	}while(next);
}

int append(s_node* list, int value){
	/*
	 * Just edits the last node's next
	 * value to a new heap allocated 
	 * node
	 */
	s_node* current = list->next;
	while(current->next)
		current = current->next;

	s_node* new = malloc(sizeof(s_node));
	if(!new)
		return -1;	
	new->data = value;
	new->prev = current;
	new->next = NULL;

	current->next = new;
	return 0;
}

int push(s_node** list, int value){
	/*
	 * Heap allocates a new node
	 * Then sets the first node's 
	 * previous to this address
	 * and this' next address to
	 * previous first node
	 */

	s_node* new = malloc(sizeof(s_node));
	if(!new)
		return -1;

	new->data = value;
	new->next = *list;
	new->prev = NULL;

	(*list)->prev = new;

	*list = new;	
	return 0;
}

void pop(s_node** list){
	/*
	 * 2nd item prev = NULL
	 * Set list start node
	 * to 2nd item
	 * Free the first node 
	 * memory
	 * 
	 * Note: the memory is 
	 * getting freed at the
	 * end anyway, so there
	 * is no point free'ing 
	 * here.
	 */

	s_node* new_head = (*list)->next;
	new_head->prev = NULL;

	free(*list);
	*list = new_head;
}

void remove_last(s_node* list){
	/*
	 * Find the last item
	 * Find the item before 
	 * change .next to NULL
	 * free last item
	 *
	 * Again, free'ing memory
	 * is done at the end 
	 */
	
	s_node* point = list;
	while(point->next)
		point = point->next;
	
	(point->prev)->next = NULL;
	free(point);
}

int remove_by_index(s_node* list, int index){
	/*
	 * Removes a node by index
	 * stitches adjacent nodes
	 * then frees memory
	 */

	int count = 0;
	s_node* current = list;
	while(current = current->next){
		if(count == index){
			// For clarity, otherwise it can
			// be done without assignment
			s_node* prev = current->prev;
			s_node* next = current->next;

			// Stitch them together
			if(prev) prev->next = next;
			if(next) next->prev = prev;
			
			free(current);
			return 0;
		}
		++count;
	}
	return -1;
}

int remove_by_node(s_node* list, s_node item){
	/*
	 * Removes item from list by 
	 * reference node
	 *
	 * returns 0 on success
	 * returns -1 on failure
	 */
	s_node* current = list;
	while(current = current->next){
		if(current->next == item.next &&
	    	   current->prev == item.prev &&
		   current->data == item.data){
			
			// For clarity, otherwise it can
			// be done without assignment
			s_node* next = current->next;
			s_node* prev = current->prev;

			// Stitch them together
			if(next) next->prev = prev;
			if(prev) prev->next = next;
			
			free(current);
			return 0;
		}		
	}
	return -1;
}

int remove_by_value(s_node* list, int value){
	/*
	 * Removes first occurance of 
	 * value in the list
	 *
	 * Returns 0 on success
	 * Returns -1 on error
	 */
	s_node* current = list;
	while(current = current->next){
		if(current->data == value){
			// For clarity, otherwise it can
			// be done without assignment
			s_node* next = current->next;
			s_node* prev = current->prev;

			//Stitch them together
			if(next) next->prev = prev;
			if(prev) prev->next = next;

			free(current);
			
			return 0;
		}
	}
	return -1;
}

s_node* get_node(s_node* list, int index){
	/* 
	 * Gets the s_node item at 
	 * index and returns 
	 * PTR to it
	 *
	 * If the function fails,
	 * NULL_PTR is returned
	 */

	int count = 0;
	s_node* next = list;
	while(next = next->next){
		if(count == index)
			return next;
		
		++count;
	}
	return NULL;
}

int get_index(s_node* list, s_node item){
	/*
	 * Iterates over each item
	 * then checks each member
	 * if all members match
	 * return count
	 *
	 * On fail, return -1
	 */

	int count = 0;
	s_node* next = list;
	while(next = next->next){
		if (
		next->prev == item.prev &&
		next->next == item.next &&
		next->data == item.data
		)
			return count;
		
		++count;
	}
	return -1;
}

void print_list(s_node* list, bool do_data, bool do_count, bool do_next, bool do_prev){
	/*
	 * Output and format
	 */

	int count = 0;
	s_node* point = list;

	do{
		if(do_count)
			printf("\nPos:  %d\n", count);
		if(do_data)
			printf("Data: %d\n", point->data);
		if(do_next)
			printf("Next: 0x%x\n", point->next);
		if(do_prev)
			printf("Prev: 0x%x\n", point->prev);
		++count;
		
	}while(point = point->next);
}

int main(int argc, char *argv[]){
 	// TO ADD: 
	// Append_list
	
	s_node* list = make_list(10, 31337);

	print_list(list, 1, 0, 0, 0);	
	free_list(list);
	return 0;
}


