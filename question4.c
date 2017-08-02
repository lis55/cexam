#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// data structure of a node
struct Node
{
char name[256];
// the name of the node
struct Node *Next; // pointer to the next node
};
// the start of the linked list
struct Node *LinkedList=NULL;

void InsertNode(char *name)
{
	struct Node *temp;
	temp=LinkedList;
	LinkedList=(struct Node*)calloc(1,sizeof(struct Node));
	LinkedList->Next=temp;
	strcpy(LinkedList->name,name);
}

void PrintList(void)
{
	int nr;
	struct Node *temp;
	nr=0;
	temp=LinkedList;
	while(temp)
	{
		printf("Node number: %d name: %s\n",nr++,temp->name);
		temp=temp->Next;
	}
}

void DeleteNode(char *name)
{
	struct Node *temp;
	temp=LinkedList;
	if(temp && strncmp(name, temp->name, 256) == 0)
	{
		LinkedList = temp->Next;
		free(temp);
		return;
	}
	struct Node *prev = NULL;
	while(temp && strncmp(name, temp->name, 256) != 0)
	{
		prev = temp;
		temp=temp->Next;
	}
	if(temp)
	{
		prev->Next = temp->Next;
		free(temp);
	}
}

void InsertNodeAtEnd(char *name)
{
	if(!LinkedList) 
	{
		LinkedList = (struct Node*)calloc(1,sizeof(struct Node));
		strcpy(LinkedList->name,name);
		return;
	}
	struct Node *temp;
	temp=LinkedList;
	while(temp->Next) 
	{
		temp = temp->Next;
	}
	temp->Next=(struct Node*)calloc(1,sizeof(struct Node));
	strcpy(temp->Next->name,name);
}

void sort()
{
	int sorted = 1;
	struct Node *temp = LinkedList;
	struct Node *prev = NULL;
	while(sorted != 0)
	{
		sorted = 0;
		temp = LinkedList;
		prev = NULL;
		while(temp && temp->Next) 
		{
			if(strncmp(temp->name, temp->Next->name, 256) > 0)
			{
				sorted = 1;
				if(prev) 
				{
					prev->Next = temp->Next;
					temp->Next = temp->Next->Next;
					prev->Next->Next = temp;
				} else {
					LinkedList = LinkedList->Next;
					temp->Next = temp->Next->Next;
					LinkedList->Next = temp;					
				}
			}
			prev = temp;
			temp = temp->Next;
		}
	}
}

int main(void)
{
	InsertNode("node one");
	InsertNode("node two");
	InsertNode("node three");
	PrintList();
	DeleteNode("node three");
	PrintList();
	DeleteNode("node one");
	PrintList();
	InsertNodeAtEnd("node four");
	PrintList();
	DeleteNode("node two");
	DeleteNode("node four");
	InsertNodeAtEnd("node one");
	PrintList();
	DeleteNode("node one");
	InsertNode("F");
	InsertNode("D");
	InsertNode("E");
	InsertNode("A");
	InsertNode("C");
	InsertNode("B");
	sort();
	PrintList();
	return 0;
}


