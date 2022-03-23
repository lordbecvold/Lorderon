//Lorderon Server core Dev by Lordbecvold
#ifndef __INC_METIN_II_GAME_POOL_H__
#define __INC_METIN_II_GAME_POOL_H__
#ifdef M2_USE_POOL

template<typename T>
struct PoolNode {
	T* block;
	PoolNode* next;
};

template<typename T>
struct PoolAllocation {
	T* chunk;
	size_t num_blocks;
	PoolNode<T>* nodes;
};

template<typename T>
struct PoolDetail {
	typedef T* PointerType;
	typedef T* ArithmeticPointerType;
	static PointerType Alloc(size_t num) {
		return new T[num];
	}
	static void Free(PointerType p) {
		delete[] p;
	}
};

template<>
struct PoolDetail<void> {
	typedef void* PointerType;
	typedef char* ArithmeticPointerType;
	static PointerType Alloc(size_t num) {
		return ::malloc(num);
	}
	static void Free(PointerType p) {
		::free(p);
	}
};

template<typename T>
class ArrayPool {
public:
	ArrayPool(size_t array_size, size_t initial_capacity = 0) : free_(NULL), array_size_(array_size), capacity_(0), alloc_count_(0), alloc_index_of_last_release_(0) {
		assert(array_size_ != 0);
		if (initial_capacity != 0) {
			Reserve(initial_capacity);
		}
	}
	~ArrayPool() {
		CleanUp();
	}
	T* Acquire() {
		if (free_ == NULL) {
			if (Stretch(capacity_) == false) {
				return NULL;
			}
		}
		assert(free_ != NULL);
		PointerType p = free_->block;
		free_ = free_->next;
		return p;
	}
	void Release(T* p) {
		if (p == NULL) {
			return;
		}
		size_t index = alloc_index_of_last_release_;
		for (size_t i = 0; i < alloc_count_; ++i, ++index) {
			if (index >= alloc_count_) {
				index = 0;
			}
			AllocationType& alloc = allocated_[index];
			ArithmeticPointerType ptr = static_cast<ArithmeticPointerType>(p);
			ArithmeticPointerType begin = static_cast<ArithmeticPointerType>(alloc.chunk);
			ArithmeticPointerType end = begin + (array_size_ * alloc.num_blocks);
			if (begin <= ptr && ptr < end) {
				size_t node_index = (ptr - begin) / array_size_;
				NodeType* node = alloc.nodes + node_index;
				assert(node->block == p);
				if (node->block != p) {
					break;
				}
				node->next = free_;
				free_ = node;
				alloc_index_of_last_release_ = index;
				break;
			}
		}
	}
	void Reserve(size_t n) {
		if (n <= capacity_) {
			return;
		}
		Stretch(n - capacity_);
	}
	void CleanUp() {
		if (alloc_count_ == 0) {
			return;
		}
		while (alloc_count_ != 0) {
			AllocationType& alloc = allocated_[--alloc_count_];
			DetailType::Free(alloc.chunk);
			delete[] alloc.nodes;
		}
		capacity_ = 0;
		free_ = NULL;
	}
	size_t array_size() const { return array_size_; }
	size_t capacity() const { return capacity_; }

private:
	typedef PoolNode<T> NodeType;
	typedef PoolAllocation<T> AllocationType;
	typedef PoolDetail<T> DetailType;
	typedef typename DetailType::PointerType PointerType;
	typedef typename DetailType::ArithmeticPointerType ArithmeticPointerType;
	static const size_t kMaxAllocCount = sizeof(size_t) * CHAR_BIT;
	bool Stretch(size_t increment) {
		if (increment == 0) {
			++increment; 
		}
		if (alloc_count_ >= kMaxAllocCount) {
			return false;
		}
		ArithmeticPointerType p = static_cast<ArithmeticPointerType>(DetailType::Alloc(array_size_ * increment));
		assert(p != NULL);
		if (p == NULL) {
			return false;
		}
		NodeType* node = new NodeType[increment];
		assert(node != NULL);
		if (node == NULL) {
			DetailType::Free(p);
			return false;
		}

		AllocationType& alloc = allocated_[alloc_count_++];
		alloc.chunk = p;
		alloc.num_blocks = increment;
		alloc.nodes = node;
		NodeType* tail = free_;
		NodeType** link = &free_;
		for (size_t i = 0; i < increment ; ++i, ++node, p += array_size_) {
			node->block = p;
			*link = node;
			link = &(node->next);
		}
		*link = tail;
		capacity_ += increment;
		return true;
	}
	NodeType* free_;
	size_t array_size_;
	size_t capacity_;
	AllocationType allocated_[kMaxAllocCount];
	size_t alloc_count_;
	size_t alloc_index_of_last_release_;
	ArrayPool(const ArrayPool&);
	void operator=(const ArrayPool&);
};

typedef ArrayPool<void> Pool;

class MemoryPool {
public:
	MemoryPool() {}
	~MemoryPool() {
		PoolMapType::iterator it = pools_.begin(), end = pools_.end();
		for ( ; it != end; ++it) {
			delete (it->second);
		}
	}
	void* Acquire(size_t size) {
		Pool* pool;
		PoolMapType::iterator it = pools_.find(size);
		if (it != pools_.end()) {
			pool = it->second;
		} else {
			pool = new Pool(size);
			pools_.insert(PoolMapType::value_type(size, pool));
		}
		return pool->Acquire();
	}
	void Release(void* p, size_t size) {
		PoolMapType::iterator it = pools_.find(size);
		if (it == pools_.end()) {
			return;
		}
		Pool* pool = it->second;
		pool->Release(p);
	}
private:
	typedef TR1_NS::unordered_map<size_t, Pool*> PoolMapType;
	PoolMapType pools_;
};

template<class T> 
class ObjectPool {
public:
	ObjectPool(size_t initial_capacity = 0) : pool_(sizeof(T), initial_capacity) {}
	~ObjectPool() {}
	T* Construct() {
		void* p = pool_.Acquire();
		if (p == NULL) {
			return NULL;
		}
		return new (p) T();
	}
	void Destroy(T* p) {
		if (p == NULL) {
			return;
		}
		p->~T();
		pool_.Release(p);
	}

	void Reserve(size_t n) {
		pool_.Reserve(n);
	}

private:
	Pool pool_;
	ObjectPool(const ObjectPool&);
	void operator=(const ObjectPool&);
};
#endif
#endif 
