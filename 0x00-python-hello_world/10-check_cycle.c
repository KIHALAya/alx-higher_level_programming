#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: the list to check whether it has a cycle in it or not.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *runner = list;

	while (runner != NULL && runner->next != NULL)
	{
		current = current->next;
		runner = runner->next->next;

		if (current == runner)
			return (1);
	}

	return (0);
}
