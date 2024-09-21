# Arrays

- Arrays provide a mechanism for storing information in adjacent or contiguous and indexable bins.
- Seeing as how they are adjacent, we can access individual bins by computing their offset from the first element and
  reading the memory in that location.
- This requires just a single memory lookup regardless of which bin we look up.
- Ordered relationship

## Array Indexing and Memory Address Calculation

The formula:
Location(i) = Location(start of array) + (Size of each element × i)

is used to compute the **memory address** (or location) of an element in an array. Let’s break it down step by step.

## 1. Arrays and Memory Layout

- An array is a collection of elements (e.g., integers, characters, or structures) that are stored **contiguously** in
  memory. This means that all elements are stored one after the other, with no gaps between them.

- Each element in the array has a fixed size, which depends on the data type. For example:
    - An `int` typically takes 4 bytes.
    - A `char` typically takes 1 byte.

## 2. Understanding the Formula

Let’s interpret the components of the formula:

- **`Location(i)`**: This is the memory address of the **i-th** element in the array (i.e., the element at index `i`).

- **`Location(start of array)`**: This is the memory address where the array begins. It's the location of the **first
  element** in the array (at index `0`).

- **`Size of each element`**: This is the size of each element in the array, measured in bytes. For instance, if it's an
  array of integers, this size would be 4 bytes.

- **`i`**: This is the **index** of the element you want to find. It indicates how many elements away from the start of
  the array the desired element is.

## 3. How the Formula Works

The formula is essentially calculating **how far** the element at index `i` is from the **start of the array**, and then
adding that to the address of the start of the array.

### Step-by-Step Explanation:

1. **Start of the Array**:
   The array begins at a specific memory address, which we call `Location(start of array)`.

2. **Offset Calculation**:
   To find the address of the element at index `i`, you need to move `i` elements forward from the start of the array.
   The size of each element determines how far to move for each step. So, you multiply the **index `i`** by the **size
   of each element** to find the total offset in memory.

3. **Final Location**:
   You add the offset to the address of the start of the array to get the memory location of the element at index `i`.

## 4. Example

Let’s assume you have an array of integers:

```c
int arr[] = {10, 20, 30, 40};  // An array of 4 integers
```

| Index | Value | Memory Address            |
|-------|-------|---------------------------|
| 0     | 10    | `0x1000` (start of array) |
| 1     | 20    | `0x1004`                  |
| 2     | 30    | `0x1008`                  |
| 3     | 40    | `0x100C`                  |

## Limitations of Arrays

- One major limitation of arrays is their fixed size and layout in memory.
- The size of an array is defined and fixed at the time of creation.
- If we need more storage, a larger array would be required and the data from the previous array will be copied over to
  the new array, with some memery wasted.
- If we have unmoving upper bound on the number of items we have to store, it is acceptable as we would only be setting
  individual entities all day.
- Fixed sized arrays can't grow with the data
- We cannot easily insert an element at the middle of an array even if there is enough space at the end of the array.  
- We would still have to shift the items over to the end to accommodate the new item to be inserted.
- Inserting an item at the middle of a full array would have a big overhead of allocation, copying and shifting.
- However, most applications require dynamic arrays
- Imagine, a word processor with fixed number of characters, a spreadsheet application with a fixed number of rows or
  columns, a photo storage that can only store a limited number of photos.



