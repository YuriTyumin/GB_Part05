1. Какими преимуществами и недостатками обладают гипервизоры первого типа по сравнению с гипервизорами второго типа?
+ меньше "прослоек" -> бОльшая производительность
- ограниченный набор поддерживаемого аппаратного обеспечения



2. Благодаря чему гипервизоры первого типа оказываются более эффективными, чем гипервизоры второго типа?
Меньше слоев абстракции


3. * Установите гипервизор VMware ESXi на доступный компьютер или виртуальную машину и выполните измерения производительности основной ОС и такой же ОС, установленной в гипервизоре.
*****************
***ОСНОВНАЯ ОС***
*****************
 System Information


  PROCESSOR:          Intel Core i5-4670 @ 3.80GHz
    Core Count:       4
    Extensions:       SSE 4.2 + AVX2 + AVX + RDRAND + FSGSBASE
    Cache Size:       6 MB
    Microcode:        0x28
    Core Family:      Haswell
    Scaling Driver:   intel_cpufreq schedutil

  GRAPHICS:           ASUS Intel HD 4600 2GB
    Frequency:        1200MHz
    OpenGL:           4.5 Mesa 21.1.1
    Vulkan:           1.2.168
    Monitor:          PHL 243V5
    Screen:           3840x1080

  MOTHERBOARD:        ASUS H97-PLUS
    BIOS Version:     2306
    Chipset:          Intel 4th Gen Core DRAM
    Audio:            Intel Xeon E3-1200 v3/4th
    Network:          Realtek RTL8111/8168/8411

  MEMORY:             16GB

  DISK:               500GB Seagate ST500DM002-1BD14
                      + 500GB Western Digital WD5000AAKS-0
                      + 250GB Samsung SSD 860
    File-System:      ext4
    Mount Options:    relatime rw seclabel
    Disk Scheduler:   BFQ
    Disk Details:     Block Size: 4096

  OPERATING SYSTEM:   Fedora 34
    Kernel:           5.12.8-300.fc34.x86_64 (x86_64)
    Desktop:          KDE Plasma 5.21.5
    Display Server:   X Server 1.20.11
    Compiler:         Clang 12.0.0
    Security:         SELinux
                      + itlb_multihit: KVM: Mitigation of VMX disabled
                      + l1tf: Mitigation of PTE Inversion; VMX: conditional cache flushes SMT disabled
                      + mds: Mitigation of Clear buffers; SMT disabled
                      + meltdown: Mitigation of PTI
                      + spec_store_bypass: Mitigation of SSB disabled via prctl and seccomp
                      + spectre_v1: Mitigation of usercopy/swapgs barriers and __user pointer sanitization
                      + spectre_v2: Mitigation of Full generic retpoline IBPB: conditional IBRS_FW STIBP: disabled RSB filling
                      + srbds: Mitigation of Microcode
                      + tsx_async_abort: Not affected

    Would you like to save these test results (Y/n): Y
    Enter a name for the result file: fedora34
    Enter a unique name to describe this test run / configuration:

If desired, enter a new description below to better describe this result set / system configuration under test.
Press ENTER to proceed without changes.

Current Description: Intel Core i5-4670 testing with a ASUS H97-PLUS (2306 BIOS) and ASUS Intel HD 4600 2GB on Fedora 34 via the Phoronix Test Suite.

New Description:

        [Performance Tip] The powersave CPU scaling governor is currently in use. It's possible to obtain greater performance if using the performance governor.

        To change behavior, run:

        echo performance | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor

        Reference: https://openbenchmarking.org/result/1706268-TR-CPUGOVERN32


        To stop showing performance tips, run: phoronix-test-suite unload-module perf_tips

        Continuing in 5 seconds or press CTRL-C to stop the testing process.

PyBench 2018-02-16:
    pts/pybench-1.1.3
    Test 1 of 1
    Estimated Trial Run Count:    3
    Estimated Time To Completion: 7 Minutes [13:25 UTC]
        Started Run 1 @ 13:18:57
        Started Run 2 @ 13:19:36
        Started Run 3 @ 13:20:15

    Total For Average Test Times:
        1494
        1507
        1501

    Average: 1501 Milliseconds
    Deviation: 0.43%

    Comparison to 9,607 OpenBenchmarking.org samples since 26 February 2011; median result: 1463. Box plot of samples:
    [                        *                  |*-----------------------------------------------*----------*----------*--------*-----*--------------------*-------------########*#*#*#*|*    ]
                                                                                                                                               This Result (48th Percentile): 1501 ^
                         Intel Atom C2750: 18183 ^                        Intel Atom N450: 12021 ^              Phytium FT1500A: 7327 ^  ARMv8 rev 3: 4613 ^   Intel Core i9-11900K: 707 ^
                             ^ ARMv7 rev 4: 20726                                                 Intel Pentium 4 2.66GHz: 8008 ^                             Intel Core i7-7700K: 959 ^
                                                                                                     ARMv7 rev 1: 9148 ^                                     2 x AMD EPYC 7402: 1216 ^
                                                                                    Intel Atom E3815: 10577 ^                                           Intel Core i7-3770: 1729 ^

    Do you want to view the results in your web browser (Y/n): Y
    Would you like to upload the results to OpenBenchmarking.org (y/n): n

******************************
***ОС В ГИПЕРВИЗОРЕ PROXMOX***
******************************
System Information


  PROCESSOR:          Common KVM
    Core Count:       2
    Extensions:       SSE 2
    Cache Size:       16 MB
    Microcode:        0x1
    Core Family:      Family 15 Model 6

  GRAPHICS:           bochs-drmdrmfb
    Monitor:          QEMU Monitor
    Screen:           1024x768

  MOTHERBOARD:        QEMU Standard PC
    BIOS Version:     rel-1.14.0-0-g155821a1990b-prebuilt.qemu.org
    Chipset:          Intel 440FX 82441FX PMC
    Network:          Red Hat Virtio device

  MEMORY:             2048MB

  DISK:               34GB QEMU HDD
    File-System:      ext4
    Mount Options:    relatime rw
    Disk Scheduler:   NONE
    Disk Details:     Block Size: 4096

  OPERATING SYSTEM:   Debian 10
    Kernel:           5.10.0-5mx-amd64 (x86_64)
    Desktop:          KDE Plasma
    Display Server:   X Server 1.20.10
    Compiler:         GCC 8.3.0
    System Layer:     KVM
    Security:         itlb_multihit: KVM: Mitigation of VMX unsupported
                      + l1tf: Mitigation of PTE Inversion
                      + mds: Vulnerable: Clear buffers attempted no microcode; SMT Host state unknown
                      + meltdown: Mitigation of PTI
                      + spec_store_bypass: Vulnerable
                      + spectre_v1: Mitigation of usercopy/swapgs barriers and __user pointer sanitization
                      + spectre_v2: Mitigation of Full generic retpoline STIBP: disabled RSB filling
                      + srbds: Not affected
                      + tsx_async_abort: Not affected

    Would you like to save these test results (Y/n): Y
    Enter a name for the result file: MXLinux_pybench
    Enter a unique name to describe this test run / configuration:

If desired, enter a new description below to better describe this result set / system configuration under test.
Press ENTER to proceed without changes.

Current Description: KVM testing on Debian 10 via the Phoronix Test Suite.

New Description:

        [Performance Tip] The powersave CPU scaling governor is currently in use. It's possible to obtain greater performance if using the performance governor.

        To change behavior, run:

        echo performance | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor

        Reference: https://openbenchmarking.org/result/1706268-TR-CPUGOVERN32


        To stop showing performance tips, run: phoronix-test-suite unload-module perf_tips

        Continuing in 5 seconds or press CTRL-C to stop the testing process.

PyBench 2018-02-16:
    pts/pybench-1.1.3
    Test 1 of 1
    Estimated Trial Run Count:    3
    Estimated Time To Completion: 7 Minutes [14:08 UTC]
        Started Run 1 @ 14:02:45
        Started Run 2 @ 14:03:50
        Started Run 3 @ 14:04:53

    Total For Average Test Times:
        2589
        2593
        2600

    Average: 2594 Milliseconds
    Deviation: 0.21%

    Comparison to 9,817 OpenBenchmarking.org samples since 26 February 2011; median result: 1466. Box plot of samples:
    [                        *                  |*-----------------------------------------------*----------*----------*--------*-----*--------------------*-------------##*#######*#*#*|*    ]
                                                                                                                                       This Result (29th Percentile): 2594 ^
                         Intel Atom C2750: 18183 ^                        Intel Atom N450: 12021 ^              Phytium FT1500A: 7327 ^  ARMv8 rev 3: 4613 ^   Intel Core i9-11900K: 707 ^
                             ^ ARMv7 rev 4: 20726                                                 Intel Pentium 4 2.66GHz: 8008 ^                             Intel Core i7-7700K: 959 ^
                                                                                                     ARMv7 rev 1: 9148 ^                                     2 x AMD EPYC 7402: 1216 ^
                                                                                    Intel Atom E3815: 10577 ^                                             Intel Core i5-4430: 1471 ^

    Do you want to view the text results of the testing (Y/n): y
MXLinux_pybench
KVM testing on Debian 10 via the Phoronix Test Suite.


Common KVM - bochs-drmdrmfb - QEMU Standard PC:

	Processor: Common KVM (2 Cores), Motherboard: QEMU Standard PC (i440FX + PIIX 1996) (rel-1.14.0-0-g155821a1990b-prebuilt.qemu.org BIOS), Chipset: Intel 440FX 82441FX PMC, Memory: 2048MB, Disk: 34GB QEMU HDD, Graphics: bochs-drmdrmfb, Monitor: QEMU Monitor, Network: Red Hat Virtio device

	OS: Debian 10, Kernel: 5.10.0-5mx-amd64 (x86_64), Desktop: KDE Plasma, Display Server: X Server 1.20.10, Compiler: GCC 8.3.0, File-System: ext4, Screen Resolution: 1024x768, System Layer: KVM


    PyBench 2018-02-16
    Total For Average Test Times
    Milliseconds < Lower Is Better
    Common KVM - bochs-drmdrmfb - QEMU Standard PC . 2594 |====================================================================================================================================

    Would you like to upload the results to OpenBenchmarking.org (y/n): n