#include "lists.h"

/**
 * check_cycle - this checks if a linked list has a cycle in it
 * @list: the linked list to check
 * Retutn: 0 if there is no cycle, and 1 if there is
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}


