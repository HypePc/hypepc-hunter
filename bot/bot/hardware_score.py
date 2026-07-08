GPU_SCORE = {
    "RTX 4090": 100,
    "RTX 4080": 90,
    "RTX 4070 Ti": 85,
    "RTX 4070": 78,
    "RTX 3080": 75,
    "RTX 3070": 65,
    "RTX 3060 Ti": 55,
    "RTX 4060": 50,
    "RTX 3060": 45,
    "RTX 2070 Super": 40,
}


CPU_SCORE = {
    "Ryzen 7 7800X3D": 100,
    "i9-14900K": 98,
    "i7-14700K": 95,
    "Ryzen 7 5800X3D": 90,
    "Ryzen 7 5700X3D": 85,
    "i5-14600K": 85,
    "Ryzen 5 7600": 82,
    "Ryzen 5 5600X": 70,
    "Ryzen 5 5600": 67,
}


def get_gpu_score(gpu):
    return GPU_SCORE.get(gpu, 0)


def get_cpu_score(cpu):
    return CPU_SCORE.get(cpu, 0)
