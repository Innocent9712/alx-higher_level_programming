#include "lists.h"
/**
 * insert_node - insert items into a sorted list in the right position
 * @head: address of the list
 * @number: number to put in node
 *
 * Return: address of the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *temp;

	current = *head;
	temp = (listint_t *) malloc(sizeof(listint_t));
	temp->n = number;
	if (current == NULL || current->n >= number)
	{
		temp->next = current;
		*head = temp;
		return (temp);
	}
	while (current && current->next && current->next->n < number)
		current = current->next;
	temp->next = current->next;
	current->next = temp;

	return (temp);
}
