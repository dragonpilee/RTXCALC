extern "C" {

__global__ void add(float *a, float *b, float *c) {
    int idx = threadIdx.x + blockDim.x * blockIdx.x;
    if (idx < 1) c[idx] = a[idx] + b[idx];
}

__global__ void sub(float *a, float *b, float *c) {
    int idx = threadIdx.x + blockDim.x * blockIdx.x;
    if (idx < 1) c[idx] = a[idx] - b[idx];
}

__global__ void mul(float *a, float *b, float *c) {
    int idx = threadIdx.x + blockDim.x * blockIdx.x;
    if (idx < 1) c[idx] = a[idx] * b[idx];
}

__global__ void divide(float *a, float *b, float *c) {
    int idx = threadIdx.x + blockDim.x * blockIdx.x;
    if (idx < 1 && b[idx] != 0) c[idx] = a[idx] / b[idx];
}

}
