// Merge Two Sorted Lists

// https://leetcode.com/explore/featured/card/top-interview-questions-easy/93/linked-list/771/

// Merge two sorted linked lists and return it as a new list. The new list
// should be made by splicing together the nodes of the first two lists.

// Example:
// Input: 1->2->4, 1->3->4
// Output: 1->1->2->3->4->4

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
  int data;
  struct Node *next;
} Node;

typedef struct List {
  Node *head;
} List;

void insert(List *list, int data) {
  Node *node = (Node *)malloc(sizeof(Node));
  node->data = data;
  node->next = list->head;
  list->head = node;

  return;
}

List *merge(List *list_1, List *list_2) {
  List *merged_list = (List *)malloc(sizeof(List));

  Node *ptr_1 = list_1->head;
  Node *ptr_2 = list_2->head;
  Node *ptr_max;
  Node *ptr_merged = NULL;

  while (ptr_1 != NULL && ptr_2 != NULL) {
    if (ptr_1->data < ptr_2->data) {
      ptr_max = ptr_1;
      ptr_1 = ptr_1->next;
    } else {
      ptr_max = ptr_2;
      ptr_2 = ptr_2->next;
    }

    if (ptr_merged == NULL) {
      merged_list->head = ptr_max;
    } else {
      ptr_merged->next = ptr_max;
    }
    ptr_merged = ptr_max;
  }

  if (ptr_1 != NULL) {
    ptr_merged->next = ptr_1;
  } else if (ptr_2 != NULL) {
    ptr_merged->next = ptr_2;
  } else {
    ptr_merged->next = NULL;
  }

  return merged_list;
}

bool assert_list(List *list, int arr[], int size) {
  Node *ptr = list->head;

  for (int i = 0; i < size; i++) {
    if (ptr == NULL) {
      return false;
    }

    if (ptr->data != arr[i]) {
      return false;
    }

    ptr = ptr->next;
  }

  return true;
}

void test() {
  List *list_1 = (List *)malloc(sizeof(List));
  list_1->head = NULL;
  insert(list_1, 10);
  insert(list_1, 8);
  insert(list_1, 7);
  insert(list_1, 6);
  insert(list_1, 3);

  List *list_2 = (List *)malloc(sizeof(List));
  list_2->head = NULL;
  insert(list_2, 9);
  insert(list_2, 5);
  insert(list_2, 4);
  insert(list_2, 2);
  insert(list_2, 1);

  List *merged_list = merge(list_1, list_2);
  int test_arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
  assert_list(merged_list, test_arr, 10) == true ? printf("passed\n")
                                                 : printf("failed\n");

  return;
}

int main() {
  test();

  return 0;
}