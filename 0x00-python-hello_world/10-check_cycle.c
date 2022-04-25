#include "lists.h"
#include <stdio.h>
/**
* check_cycle - function that checks if the cycle of the 
* linked list exist or not
* Return: 0 if there is no a cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *nextnextnode = list;
	listint_t *nextnode = list;
	
	while (1)
	{
		if (nextnode != NULL && nextnextnode != NULL && list != NULL)
		{
			nextnode = nextnode->next;
			nextnextnode = nextnextnode->next->next;
	
			if (nextnode == nextnextnode)
				return (1);
			else
				break;
		}
		else
			return (0);
	}
}
