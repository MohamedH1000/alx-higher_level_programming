#include "lists.h"
/**
* l_l - a function that know the number of nodes
* in a list
* @head : pointer to head of alinked list
* Return: number of nodes in a linked list
*/
size_t l_l(listint_t *head)
{
	size_t  n = 0;

	if (head == NULL)
		return (0);
	while (head != NULL)
	{
		n++;
		head = head->next;
	}
	return (n);
}
/**
* is_palindrome - a function that checks if a linked list
* is palindrome or not
* @head: a double pointer to the head of a list
* Return: 0 if not pal and 1 if its pal
*/
int is_palindrome(listint_t **head)
{
	int *tnazr, a = 0, b = 0, len = 0;
	listint_t *moakt;

	if (*head == NULL)
		return (1);
	moakt = *head;
	len = l_l(moakt);
	tnazr = (int *)malloc(sizeof(int) * len);
	if (tnazr == NULL)
		return (2);
	moakt = *head;
	while (moakt != NULL)
	{
		tnazr[b] = moakt->n;
		b++;
		moakt = moakt->next;
	}
	for (a = 0, b = len - 1; a < b; a++, b--)
	{
		if (tnazr[a] != tnazr[b])
			return (0);
	}
	return (1);
}
