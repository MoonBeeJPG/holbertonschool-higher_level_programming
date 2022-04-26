#include "lists.h"
#include <stdio.h>
/**
* check_cycle - function that checks if the cycle of the
* linked list exist or not
*
* @list: List to check
*
* Return: 0 if there is no a cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
listint_t *nextnextnode = list, *nextnode = list;
	while (nextnextnode->next != NULL && nextnextnode->next->next != NULL && list != NULL)
	{
		nextnode = nextnode->next;
		nextnextnode = nextnextnode->next->next;
		if (nextnode == nextnextnode)
			return (1);
	}
	return(0);
}
