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

  if (list->head == NULL) {
    node->next = node;
    list->head = node;

    return;
  }

  Node *ptr = list->head;
  while (ptr->next != list->head) {
    ptr = ptr->next;
  }

  ptr->next = node;
  node->next = list->head;
  list->head = node;

  return;
}

int size(List *list) {
  if (list->head == NULL) {
    return 0;
  }

  Node *ptr = list->head;
  int count = 0;

  do {
    ptr = ptr->next;
    count++;
  } while (ptr != list->head);

  return count;
}

bool search(List *list, int data) {
  if (list->head == NULL) {
    return false;
  }

  Node *ptr = list->head;

  do {
    if (ptr->data == data) {
      return true;
    }

    ptr = ptr->next;
  } while (ptr->next != list->head);

  return false;
}

void delete_data(List *list, int data) {
  // empty list
  if (list->head == NULL) {
    return;
  }

  // found - unit length list
  if (list->head->data == data && list->head->next == list->head) {
    list->head = NULL;
  }

  // find data node
  Node *prev_ptr = NULL, *curr_ptr = list->head;
  do {
    prev_ptr = curr_ptr;
    curr_ptr = curr_ptr->next;
  } while (curr_ptr->data != data && curr_ptr != list->head);

  // not found
  if (curr_ptr->data != data) {
    return;
  }

  // first element
  if (curr_ptr == list->head) {
    list->head = curr_ptr->next;
  }

  // anywhere in the list
  prev_ptr->next = curr_ptr->next;

  return;
}

void reverse(List *list) {
  // empty list or unit length list
  if (list->head == NULL || list->head->next == list->head) {
    return;
  }

  Node *curr_ptr = list->head, *prev_ptr = NULL, *next_ptr;

  do {
    next_ptr = curr_ptr->next;
    curr_ptr->next = prev_ptr;
    prev_ptr = curr_ptr;
    curr_ptr = next_ptr;
  } while (curr_ptr != list->head);

  list->head->next = prev_ptr;
  list->head = prev_ptr;

  return;
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

  if (ptr != list->head) {
    return false;
  }

  return true;
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

  // Delete - not found
  delete_data(list, 100);
  int test_arr_5[] = {40, 20};
  assert_list(list, test_arr_5, 2) == true ? printf("passed\n")
                                           : printf("failed\n");

  insert(list, 10);
  insert(list, 30);
  insert(list, 50);
  reverse(list);
  int test_arr_6[] = {20, 40, 10, 30, 50};
  assert_list(list, test_arr_6, 5) == true ? printf("passed\n")
                                           : printf("failed\n");

  // Reverse - empty list
  List *empty_list = (List *)malloc(sizeof(List));
  empty_list->head = NULL;
  reverse(list);
  int empty_arr[] = {};
  assert_list(empty_list, empty_arr, 0) == true ? printf("passed\n")
                                                : printf("failed\n");

  // Reverse - unit length list
  List *unit_list = (List *)malloc(sizeof(List));
  unit_list->head = NULL;
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