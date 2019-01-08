#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
  int data;
  struct Node *prev, *next;
} Node;

typedef struct List {
  struct Node *head;
} List;

void insert(List *list, int data) {
  Node *node = (Node *)malloc(sizeof(Node));

  node->data = data;
  node->prev = NULL;
  node->next = list->head;

  if (list->head != NULL) {
    list->head->prev = node;
  }
  list->head = node;

  return;
}

int size(List *list) {
  Node *ptr = list->head;

  int size = 0;
  while (ptr != NULL) {
    size++;
    ptr = ptr->next;
  }

  return size;
}

bool search(List *list, int data) {
  Node *ptr = list->head;

  while (ptr != NULL) {
    if (ptr->data == data) {
      return true;
    }

    ptr = ptr->next;
  }

  return false;
}

void delete_data(List *list, int data) {
  Node *ptr = list->head;

  while (ptr != NULL) {
    if (ptr->data == data) {
      if (ptr->prev != NULL) {
        ptr->prev->next = ptr->next;
      } else { // first element
        list->head = ptr->next;
      }
      if (ptr->next != NULL) { // not last element
        ptr->next->prev = ptr->prev;
      }
    }

    ptr = ptr->next;
  }
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

void reverse(List *list) {
  Node *ptr = list->head, *next_ptr;

  while (ptr != NULL) {
    if (ptr->next == NULL) {
      list->head = ptr;
    }

    // swap prev and next pointers
    next_ptr = ptr->next;
    ptr->next = ptr->prev;
    ptr->prev = next_ptr;

    ptr = next_ptr;
  }
}

void test() {
  List *list = (List *)malloc(sizeof(List));
  list->head = NULL;

  // Insert
  insert(list, 10);
  insert(list, 20);
  int test_arr_1[] = {20, 10};
  assert_list(list, test_arr_1, 2) == true ? printf("passed\n")
                                           : printf("failed\n");

  // Count
  insert(list, 30);
  insert(list, 40);
  insert(list, 50);
  size(list) == 5 ? printf("passed\n") : printf("failed\n");

  // Search
  search(list, 30) == true ? printf("passed\n") : printf("failed\n");
  search(list, 100) == false ? printf("passed\n") : printf("failed\n");

  // Delete - first element
  delete_data(list, 50);
  int test_arr_2[] = {40, 30, 20, 10};
  assert_list(list, test_arr_2, 4) == true ? printf("passed\n")
                                           : printf("failed\n");

  // Delete - any element
  delete_data(list, 30);
  int test_arr_3[] = {40, 20, 10};
  assert_list(list, test_arr_3, 3) == true ? printf("passed\n")
                                           : printf("failed\n");

  // Delete - last element
  delete_data(list, 10);
  int test_arr_4[] = {40, 20};
  assert_list(list, test_arr_4, 2) == true ? printf("passed\n")
                                           : printf("failed\n");

  // Reverse
  insert(list, 10);
  insert(list, 30);
  insert(list, 50);
  reverse(list);
  int test_arr_5[] = {20, 40, 10, 30, 50};
  assert_list(list, test_arr_5, 5) == true ? printf("passed\n")
                                           : printf("failed\n");

  // Reverse - empty list
  List *empty_list = (List *)malloc(sizeof(List));
  reverse(list);
  int empty_arr[] = {};
  assert_list(empty_list, empty_arr, 0) == true ? printf("passed\n")
                                                : printf("failed\n");

  // Reverse - unit length list
  List *unit_list = (List *)malloc(sizeof(List));
  insert(unit_list, 10);
  reverse(list);
  int unit_arr[] = {10};
  assert_list(unit_list, unit_arr, 1) == true ? printf("passed\n")
                                              : printf("failed\n");

  return;
}

int main() {
  test();
  return 0;
}