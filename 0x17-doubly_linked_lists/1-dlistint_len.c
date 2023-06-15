#include "lists.h"

/**
 * dlistint_len - this returns num of elements in a dlistint_t list
 * @h: pointer to the list.
 * Return: number of nodes
 */
size_t dlistint_len(const dlistint_t *h)
{
	const dlistint_t *node = h;
	size_t cont = 0;

	while (node)
	{
		node = node->next;
		cont++;
	}

	return (cont);
}
