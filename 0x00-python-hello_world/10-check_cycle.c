#include "lists.h"
/**
 * check_cycle - checks a list to know if a cycle exists
 * @list: list to check
 *
 * Return: (0) if no cycle is found and (1) if a cycle is found
 */

int check_cycle(listint_t *list)
{
	listint_t *current, *temp;

	current = list;

	while (current->next != NULL)
	{
		temp = current->next;
		while (temp->next != NULL)
		{
			if (current == temp)
				return (1);
			temp = temp->next;
		}
		current = current->next;
	}
	return (0);
}
