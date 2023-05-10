#include "lists.h"
/**
* insert_node - a function that inserts a node in
* a singly linked list
* @head:the head of a linked list
* @number: the new node data
* Return: the new node address
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nN;
	listint_t *beg;

	beg = *head;
	nN = malloc(sizeof(listint_t));
	if (nN == NULL)
	{
		return (NULL);
	}
	nN->n = number;
	nN->next = NULL;

	if (*head == NULL || beg->n > nN->n)
	{
		nN->next = *head;
		*head = nN;
		return (nN);
	}
	while (beg->next != NULL)
	{
		if ((beg->next->n > nN->n && beg->n < nN->n)
			|| nN->n == beg->n)
		{
			nN->next = beg->next;
			beg->next = nN;
			return (nN);
		}
		beg = beg->next;
	}
	nN->next = beg->next;
	beg->next = nN;
	return (nN);
}
