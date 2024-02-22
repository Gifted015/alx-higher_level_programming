#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: the head of the linked list
 * Return: 0 if it is not a palindrome and 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
  listint_t *temp = *head;
  int i, j, len = 0;
  int list[1000];

  if (temp == NULL)
    return (1);

  else
    {
      i = 0;
      while (temp != NULL)
	{
	  list[i] = (temp->n);
	  temp = temp->next;
	  i++;
	}
      len = i;
      for (i = 0, j = len - 1; i < len; i++, j--)
	{
	  if (list[i] == list[j])
	    continue;
	  else
	    return (0);
	}
      return (1);
    }
}
