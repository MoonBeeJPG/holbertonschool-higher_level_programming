#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
/**
* insert_node -  A function that inserts a number into 
* a sorted sigly linked list
*
* @head: header of the linked list
* @number: number to insert
*
* Return: The address of the new node, 
* of NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;

	if (*head == NULL)
		return (NULL);

	new_node = (listint_t *)malloc(sizeof(listint_t));

	if (new_node)
		return (NULL);
	new_node->n = number;
	new_node->next = *head;
	*head = new_node;

	return (new_node);
}
