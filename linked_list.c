#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

struct Node {
  int data;
  struct Node *next;
};

struct List {
  struct Node *head;
};

void insert(struct List *list, int data) {
  struct Node *node = (struct Node *)malloc(sizeof(struct Node));

  node->data = data;
  node->next = list->head;
  list->head = node;
}

int size(struct List *list) {
  struct Node *ptr = list->head;

  int size = 0;
  while (ptr != NULL) {
    ptr = ptr->next;
    size++;
  }

  return size;
}

bool search(struct List *list, int data) {
  struct Node *ptr = list->head;

  while (ptr != NULL) {
    if (ptr->data == data) {
      return true;
    }

    ptr = ptr->next;
  }

  return false;
}

void delete_data(struct List *list, int data) {
  // first element
  if (list->head != NULL && list->head->data == data) {
    list->head = list->head->next;
  }

  struct Node *ptr = list->head;

  while (ptr->next != NULL) {
    if (ptr->next->data == data) {
      ptr->next = ptr->next->next;
      return;
    }

    ptr = ptr->next;
  }

  return;
}

void reverse(struct List *list) {
  struct Node *ptr = list->head, *prev_ptr = NULL, *next_ptr;

  while (ptr != NULL) {
    next_ptr = ptr->next;
    ptr->next = prev_ptr;
    prev_ptr = ptr;

    ptr = next_ptr;
  }

  list->head = prev_ptr;
}

bool assert_list(struct List *list, int arr[], int size) {
  struct Node *ptr = list->head;

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
  struct List *list;
  list = (struct List *)malloc(sizeof(struct List));
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
  delete_data(list, 30);
  int test_arr_2[] = {50, 40, 20, 10};
  assert_list(list, test_arr_2, 4) == true ? printf("passed\n")
                                           : printf("failed\n");

  // Delete - any element
  delete_data(list, 50);
  int test_arr_3[] = {40, 20, 10};
  assert_list(list, test_arr_3, 3) == true ? printf("passed\n")
                                           : printf("failed\n");

  // Delete - last element
  delete_data(list, 10);
  int test_arr_4[] = {40, 20};
  assert_list(list, test_arr_4, 2) == true ? printf("passed\n")
                                           : printf("failed\n");

  // Reverse - empty list
  struct List *empty_list = (struct List *)malloc(sizeof(struct List));
  empty_list->head = NULL;
  int empty_arr[] = {};
  assert_list(empty_list, empty_arr, 0) == true ? printf("passed\n")
                                                : printf("failed\n");

  // Reverse - unit length list
  delete_data(list, 40);
  int unit_arr[] = {20};
  assert_list(list, unit_arr, 1) == true ? printf("passed\n")
                                         : printf("failed\n");

  // Reverse - non-empty list
  insert(list, 10);
  insert(list, 30);
  insert(list, 40);
  insert(list, 50);
  int test_arr_5[] = {50, 40, 30, 10, 20};
  assert_list(list, test_arr_5, 5) == true ? printf("passed\n")
                                           : printf("failed\n");
  reverse(list);
  int test_arr_6[] = {20, 10, 30, 40, 50};
  assert_list(list, test_arr_6, 5) == true ? printf("passed\n")
                                           : printf("failed\n");
}

int main() {
  test();
  return 0;
}
