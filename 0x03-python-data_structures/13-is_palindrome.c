#include "lists.h"

/**
* reverse_listint - reverses a linked list
* @head: pointer to the first node in the list
* Made by MEGATRON
* Return: pointer to the first node in the new list
*/

void reverse_listint(listint_t **head)
{
  listint_t *prev = NULL;
  listint_t *crt = *head;
  listint_t *next = NULL;

  while (crt)
    {
      next = crt->next;
      crt->next = prev;
      prev = crt;
      crt = next;
    }

  *head = prev;
}

/**
* is_palindrome - checks if a linked list is a palindrome
* @head: double pointer to the linked list
* Made by MEGATRON
* Return: 1 if it is, 0 if not
*/

int is_palindrome(listint_t **head)
{
  listint_t *slow = *head, *fast = *head, *tmp = *head, *dup = NULL;

  if (*head == NULL || (*head)->next == NULL)
    return (1);

  while (1)
    {
      fast = fast->next->next;
      if (!fast)
	{
	  dup = slow->next;
	  break;
	}
      if (!fast->next)
	{
	  dup = slow->next->next;
	  break;
	}
      slow = slow->next;
    }

  reverse_listint(&dup);

  while (dup && tmp)
    {
      if (tmp->n == dup->n)
	{
	  dup = dup->next;
	  tmp = tmp->next;
	}
      else
	return (0);
    }

  if (!dup)
    return (1);

  return (0);
}
