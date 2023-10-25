#include "lists.h"

/**
 * insert_node - inserts a new node
 * @head: head of a list.
 * @number: index of the list
 * Return: the address of the new node, or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new = malloc(sizeof(listint_t));
    if (new == NULL) {
        return NULL;
    }

    new->n = number;
    new->next = NULL;

    if (*head == NULL) {
        *head = new;
        return new;
    }

    listint_t *prev = NULL;
    listint_t *cur = *head;
    while (cur != NULL && cur->n < number) {
        prev = cur;
        cur = cur->next;
    }

    if (prev == NULL) {
        new->next = *head;
        *head = new;
    } else {
        new->next = cur;
        prev->next = new;
    }

    return new;
}
