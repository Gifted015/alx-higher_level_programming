#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: the head of the linked list
 * Return: 0 if it is not a palindrome and 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
  listint_t *temp = *head;
  int i, j;
  int *list;
  
  if (temp == NULL)
    return (1);

  else
    {
      list = (int *)malloc(o);
      while (temp != NULL)
	{
	  i = 0
	  list = (int *)realloc(list, (i + 1) * sizeof(int));
	  list[i] = (temp->n);
	  temp = temp->next;
	}
      len = len(list);
      for (i = 0, i < len, i++)
	{
	  j = (i + 1) * -1;
	  if (list[i] == list[j])
	    continue;
	  else
	    return 0;
	}
      return 1;
    }
}
