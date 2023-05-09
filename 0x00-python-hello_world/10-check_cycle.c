#include <stdio.h>
#include "lists.h"
/**
* check_cycle - a function that check a single linked list if its have a cycle
* inside it
* @list: a list of single links
* Return: if there is a cycle it return 1 otherwise it returns 0
*/
int check_cycle(listint_t *list)
{
	listint_t *t;
	listint_t *h;

	if (list == NULL)
	{
		return (0);
	}
	t = list;
	h = list;
	while (t != NULL && t->next != NULL)
	{
		h = h->next;
		t = t->next->next;
		if (h == t)
		{
			return (1);
		}

	}
	return (0);
}
