#include "lists.h"


/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 * An empty list is considered a palindrome
 */

 int is_palindrome(listint_t **head){
		listint_t *current = *head;
		int i = 0, j = 0, k = 0;
		int array[10000];
		if (head == NULL)
			return (1);
		while (current != NULL)
		{
			array[i] = current->n;
			current = current->next;
			i++;
		}
		j = i - 1;
		while (k < j)
		{
			if (array[k] != array[j])
				return (0);
			k++;
			j--;
		}
		return (1);
 }
 