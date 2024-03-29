#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - Write a function in C that inserts a number into a sorted singly linked list.
 * @head: the head of the singly linked list
 * @number: number to be added
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
  listint_t *new;
  listint_t *current;

  current = *head;

  new = malloc(sizeof(listint_t));
  if (new == NULL)
    return (NULL);

  new->n = number;
  new->next = NULL;

  if (*head == NULL)
    *head = new;
  else
    {
      if (!((current->n) > number))
      {
	while (current->next != NULL)
	  {
	    if (((current->next)->n) > number)
	      break;
	    current = current->next;
	  }
	  new->next = current->next;
	  current->next = new;
      }
      else
	{
	  new->next = current;
	  *head = new;
	}
    }

    return (new);
}
