/*!
 * @file  sorting.cpp
 * @brief Compare bubble sort and Heap sort
 * @brief My old assignment when I was in The University of Tokyo
 * @date 2017/02/10
 * @author YoonSeong Yong 
 * 
 */

#include <iostream>
#include <fstream>
#include <stdlib.h> /// for rand and exit
#include <vector>

using namespace std;
void bubblesort(vector<int> data, int count, long& bubble_sort_timer)
{
	int i, j, temp;
	for (i=0; i<count; i++)
		for (j=count-1;j>i;j--)
		{
			if (data[j-1]>data[j])
			{
				temp=data[j-1];
				data[j-1]=data[j];
				data[j]=temp;
			}
			bubble_sort_timer++;
		}
}
void shiftDown(vector<int> data, int start, int end, long& heap_sort_timer)
{
	int root=start;
	int temp;
    /// while the roots has at least one child
	while (root*2+1<=end) 
	{
        /// root*2+1 points to the left child
		int child=root*2+1;		
		int swap=root;
        
		/// keeps track of child to swap with
		if (data[swap]<data[child])
			swap=child;
		/// check if root is smaller than left child
		if (child+1<=end && data[swap]<=data[child+1])
			swap=child+1;
		/// check if right child exists, and if it's bigger than what we're currently swapping with
			if (swap!=root)
            /// check if we need to swap at all
			{
				temp=data[swap];
				data[swap]=data[root];
				data[root]=temp;
				root=swap;
				/// repeat to continue shifting down the child now
			}
			else
				return;
		heap_sort_timer++;
	}
}
void heapify(vector<int> data, int count, long& heap_sort_timer)
{
	int start=count/2-1;
	while(start>=0)
	{
		shiftDown(data, start, count-1, heap_sort_timer);
		/// shift down the node at index start to the proper place such that all nodes below the start index are in heap order
        start=start-1;
		/// after shifting down the root, all nodes/elements are in heap order
		heap_sort_timer++;
	}
}

void heapSort(vector<int> data, int count,long& heap_sort_timer)
{
    /// first place a in max-heap order
	heapify(data,count, heap_sort_timer); 
	int temp;
	int end=count-1;
	while (end>0)
	{
		temp=data[0];
		/// swap the root (maximum value) of the heap with the last elemen of the heap
			data[0]=data[end];
		data[end]=temp;
		end=end-1;
		/// decrease the size of the heap by one so that the previous max value will stay in its proper placement
			shiftDown(data,0,end,heap_sort_timer);
		/// put the heap back in max-heap order
		heap_sort_timer++;
	}
}
int main()
{
	char next;
	/// randomize all input data
	ofstream outputFile("result.csv");
	if(!outputFile)
	{
		cout<<"File could not be opened\n";
		exit(1);
	}
	outputFile<<"Size\t\t"<<"Bubble Sort\t\t"<<"Heap Sort\t\t"<<endl;
	do
	{
		int count=0;
		vector<int> data;
        /// reset the timer
		long bubble_sort_timer=0; 
		long heap_sort_timer=0;
		cout<<"How many numbers you wanna sort?: ";
		cin>>count;
		for(int i=0; i<count; i++)
			data.push_back(rand());
		bubblesort(data, count, bubble_sort_timer);
		cout<<"Calculation time by using bubble sort: "<<bubble_sort_timer<<endl;
		heapSort(data, count, heap_sort_timer);
		cout<<"Calculation time by using heap sort: "<<heap_sort_timer<<endl;
		outputFile<<count<<"\t\t"<<bubble_sort_timer<<"\t\t"<<heap_sort_timer<<endl;
		/// export all data to "result.xls"
		cout<<"Do you still wanna continue? (Press 'Y' or 'y' to continue): ";
		cin>>next;
		/// the programming is continued if 'Y' or 'y' is keyed in
		cout<<endl;
	} while(next=='Y'||next=='y');
}
