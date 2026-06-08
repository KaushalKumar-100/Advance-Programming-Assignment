/*Assignment 13: In C, managing strings is a common source of buffer overflows and memory leaks. 
Implement a Dynamic String Buffer that automatically grows as needed.

Requirements:

1. Create a StringBuffer struct containing a char *data, a size_t length, and a size_t capacity. 

2. Write a function sb_init(size_t initial_capacity) that allocates the struct and the data buffer on the heap. Handle NULL returns from malloc.

3. Write sb_append(StringBuffer *sb, const char *str).

4. If the new string exceeds current capacity, use realloc to double the capacity.
 Ensure you handle realloc safely (don't overwrite the original pointer if it returns NULL).

Write sb_free(StringBuffer *sb) which works as a destructor that frees both the internal data and the struct itself to prevent memory leaks.

Demonstrate the buffer growing at least twice and then free all memory.*/


#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char *data;
    size_t length;
    size_t capacity;
} StringBuffer;


StringBuffer* sb_init(size_t initial_capacity) {
    StringBuffer *sb = (StringBuffer *)malloc(sizeof(StringBuffer));

    if (sb == NULL) {
        printf("Memory allocation failed for StringBuffer.\n");
        return NULL;
    }

    sb->data = (char *)malloc(initial_capacity * sizeof(char));

    if (sb->data == NULL) {
        printf("Memory allocation failed for data buffer.\n");
        free(sb);
        return NULL;
    }

    sb->length = 0;
    sb->capacity = initial_capacity;
    sb->data[0] = '\0';

    return sb;
}


void sb_append(StringBuffer *sb, const char *str) {
    size_t str_len = strlen(str);

    
    while (sb->length + str_len + 1 > sb->capacity) {

        size_t new_capacity = sb->capacity * 2;

        
        char *temp = (char *)realloc(sb->data, new_capacity);

        if (temp == NULL) {
            printf("Reallocation failed.\n");
            return;
        }

        sb->data = temp;
        sb->capacity = new_capacity;

        printf("Buffer resized to capacity: %zu\n", sb->capacity);
    
    }

    
    strcat(sb->data, str);

    sb->length += str_len;
}


void sb_free(StringBuffer *sb) {
    if (sb != NULL) {
        free(sb->data);
        free(sb);
    }
}

int main() {

    
    StringBuffer *sb = sb_init(10);

    if (sb == NULL) {
        return 1;
    }

    printf("Initial Capacity: %zu\n", sb->capacity);

    
    sb_append(sb, "Hello");
    printf("String: %s\n", sb->data);

    sb_append(sb, " kaushal!");
    printf("String: %s\n", sb->data);

    sb_append(sb, " This is a kaushal kumar .");
    printf("String: %s\n", sb->data);
    sb_append(sb, " this.");
    printf("String: %s\n", sb->data);

    printf("\nFinal String: %s\n", sb->data);
    printf("Final Length: %zu\n", sb->length);
    printf("Final Capacity: %zu\n", sb->capacity);

    
    // sb_free(sb);

    // printf("\nMemory freed successfully.\n");

    return 0;
}