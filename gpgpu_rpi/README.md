# OpenCL for GPU
Early efforts to use GPUs as general-purpose processors required reformulating computational problems in terms of graphics primitives, as supported by the two 
major APIs for graphics processors, **OpenGL** and **DirectX**. This cumbersome translation was obviated by the advent of general-purpose programming languages 
and APIs such as Sh/RapidMind, Brook and Accelerator. 

This cumbersome translation was obviated by the advent of general-purpose programming languages and APIs and followed by **Nvidia's CUDA**, which allowed 
programmers to ignore the underlying graphical concepts in favor of more common high-performance computing concepts. Newer, hardware vendor-independent 
offerings include Microsoft's DirectCompute and Apple/Khronos Group's **OpenCL**. _This means that modern GPGPU pipelines can leverage the speed of a GPU 
without requiring full and explicit conversion of the data to a graphical form._

## [VideoCore](https://en.wikipedia.org/wiki/VideoCore) 
it is the processor used in the raspberry GPU owned by Broadcom
 
The references used in this project are [Raspberry Pi Playground](https://rpiplayground.wordpress.com/2014/05/03/hacking-the-gpu-for-fun-and-profit-pt-1/) blog 
and [VideoCore Wiki Note](https://github.com/hermanhermitage/videocoreiv/wiki/VideoCore-IV-Programmers-Manual)


>**OpenCL** is created specifically for computing. When you do scientific computing using **OpenGL** you always have to think about how to map your computing 
>problem to the graphics context (i.e. talk in terms of textures and geometric primitives like triangles, etc) in order to get your computation going.

## Input
**uniforms** are analogous to function call arguments.  Alternatively, you might think of them as constants from the QPU point of view, only changing between 
program invocations (initiated by the host).  The QPU gets them in a queue (i.e. in order) one at a time.  They are single word (32-bit) and they are the most 
convenient for this sort of data that is constant throughout one run.

**textures** are also single word values but they are not limited in how many you can use or the access pattern (i.e. they do not have to accessed in order).

**VPM** is a block of memory that is shared by all the QPUs and transfers occur explicitly in blocks of vectors.  We will talk much more about that later.

>for now, we will be using uniforms

## Output
to initiate a DMA transfer from the QPU VPM space to an address in the host’s memory.  This implies two things. 
- First, we’ll need another uniform to pass in the address to the block of memory where we want to write the result value back.
- second, we’ll need to write the value to the VPM first before we can DMA from the VPM to the host.  So even for “Hello World” we need to understand the VPM and VCD.

## Vectorization
Most operations on the GPU operate in a vectorized fashion: one operation can be performed on up to four values at once. For instance, if one color <R1, G1, B1> is to be modulated by another color <R2, G2, B2>, the GPU can produce the resulting color <R1*R2, G1*G2, B1*B2> in one operation. This functionality is useful in graphics because almost every basic data type is a vector (either 2-, 3-, or 4-dimensional). Examples include vertices, colors, normal vectors, and texture coordinates. Many other applications can put this to good use, and because of their higher performance, vector instructions (SIMD) have long been available on CPUs.

There are actually 12 cores inside the GPU, each one known as a QPU for Quad Processing Unit. The **VPM** (Vertex Program Memeory) memory is shared between them.
There are two **TMUs** (Texture Memory Unit) available to each core. You can manually choose how to use each if you have an algorithmic way to send the same work to both, by turning off 'TMU swap'.

The **VCD** (Vertex Cache Manager) can load blocks of scattered vectors or 2D byte arrays in memory to the VPM with both horizontal and vertical orientation. 
The separate **VDW** (VCD DMA Write) block does the reverse, storing vertical or horizontal VPM data out to 2D arrays of data in memory.
