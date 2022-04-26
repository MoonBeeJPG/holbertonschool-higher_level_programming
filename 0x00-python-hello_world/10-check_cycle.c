#include "lists.h"
/**
* check_cycle - A function that checks if a linked list has a cycle or not
*
* @list: the list to check
*
* Return: 0 if there is not a cycle. 2 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *nextnode = list, *nextnextnode = list;

	while (list != NULL && nextnextnode->next != NULL && nextnextnode->next->next != NULL)
	{
		nextnode = nextnode->next;
		nextnextnode = nextnextnode->next->next;

		if (nextnode == nextnextnode)
			return (1);
	}
	return (0);
}
