#include "lists.h"
/**
* is_palindrome - Write a function that checks if a sigly linked
* list is a palindrome
*
* @head: header of the linked list 
*
* Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
	listint_t *current = *head0;
	unsigned int i, datos[1024], tam = 0;

	if (head == NULL)
		return(0);
	if (*head == NULL)
		return(1);
	
	while (current != NULL)
	{
		current =  current->next;
		tam += 1;
	}
	if(tam == 1)
		return(1);
	current = *head;
	while (current != NULL)
	{
		datos[i++] = current->next;
		current = current->next;
	}

	for (i = 0; i <= (tam / 2); i++)
	{
		if (datos[i] != datos[tam - i - 1])
			return(0);
	}
	return(1);
}
