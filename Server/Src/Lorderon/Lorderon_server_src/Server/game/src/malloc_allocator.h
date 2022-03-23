//Lorderon Server Core Dev by Lordbecvold
#ifndef _MALLOC_ALLOCATOR_H_
#define _MALLOC_ALLOCATOR_H_

class MallocAllocator {
public:
	MallocAllocator() {}
	~MallocAllocator() {}
	void SetUp() {}
	void TearDown() {}
	void* Alloc(size_t size) {
		return ::malloc(size);
	}
	void Free(void* p) {
		::free(p);
	}
};
#endif 
