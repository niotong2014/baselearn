target: thread_incr thread_incr_mutex thread_incr_mutex_cond
thread_incr: thread_incr.c
	gcc -o thread_incr thread_incr.c -pthread
thread_incr_mutex: thread_incr_mutex.c
	gcc -o thread_incr_mutex thread_incr_mutex.c -pthread
thread_incr_mutex_cond: thread_incr_mutex_cond.c
	gcc -o thread_incr_mutex_cond thread_incr_mutex_cond.c -pthread

clean:
	rm thread_incr thread_incr.o thread_incr_mutex thread_incr_mutex.o thread_incr_mutex_cond thread_incr_mutex_cond.o
