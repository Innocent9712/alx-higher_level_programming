#include "lists.h"

/**
 * recursive_check - recursively loop through the list
 * @head: head of the list
 * @next: next item on the list
 * Description: It first goes to the end, and then recursively
 * compares each caracter from both ends
 *
 * Return: 1 if characters match or end of list 0 if not
 */

int recursive_check(listint_t **head, listint_t *next)
{
	if (next == NULL)
	{
		return (1);
	}

	if (recursive_check(head, next->next) && (*head)->n == next->n)
	{
		(*head) = (*head)->next;
		return (1);
	}
	return (0);
}

/**
 * is_palindrome - main function to run the recursive function
 * @head: head of the list
 *
 * Return: ! if is palindrome else 0
 */

int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (recursive_check(head, *head));
}
