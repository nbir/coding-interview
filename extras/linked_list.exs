defmodule LinkedList do
  def insert(list, data), do: [data | list]

  def size(list), do: size(list, 0)
  defp size([], count), do: count
  defp size([head | tail], count), do: size(tail, count + 1)

  def search([], _data), do: false
  def search([head | tail], data) when head == data, do: true
  def search([head | tail], data), do: search(tail, data)

  def delete([], _data), do: []
  def delete([head | tail], data) when head == data, do: tail
  def delete([head | tail], data), do: [head | delete(tail, data)]

  def reverse(list), do: reverse(list, [])
  defp reverse([], reversed_list), do: reversed_list
  defp reverse([head | tail], reversed_list), do: reverse(tail, [head | reversed_list])
end

print_assertion =
  &case &1 do
    true -> IO.inspect("passed")
    false -> IO.inspect("failed")
  end

assert_list = &print_assertion.(&1 == &2)
assert_count = &print_assertion.(&1 == &2)
assert_found = &print_assertion.(&1 == &2)

# Insert
LinkedList.insert([], 10) |> LinkedList.insert(20) |> assert_list.([20, 10])

# Size
LinkedList.size([]) |> assert_count.(0)
LinkedList.size([1]) |> assert_count.(1)
LinkedList.size([1, 2, 3]) |> assert_count.(3)

# Search
LinkedList.search([], 1) |> assert_found.(false)
LinkedList.search([1], 1) |> assert_found.(true)
LinkedList.search([1, 2, 3], 2) |> assert_found.(true)
LinkedList.search([1, 2, 3], 5) |> assert_found.(false)

# Delete
LinkedList.delete([], 1) |> assert_list.([])
LinkedList.delete([1], 1) |> assert_list.([])
LinkedList.delete([1, 2, 3], 1) |> assert_list.([2, 3])
LinkedList.delete([1, 2, 3], 2) |> assert_list.([1, 3])
LinkedList.delete([1, 2, 3], 3) |> assert_list.([1, 2])

# # Reverse
LinkedList.reverse([]) |> assert_list.([])
LinkedList.reverse([1]) |> assert_list.([1])
LinkedList.reverse([1, 2, 3]) |> assert_list.([3, 2, 1])
