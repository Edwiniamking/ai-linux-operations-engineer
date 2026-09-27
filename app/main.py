from app.tools.linux import get_system_info, get_disk_usage


def main():
    print("\nAI Linux Operations Engineer")
    print("=" * 40)

    print("\nSYSTEM INFORMATION")
    system = get_system_info()

    for key, value in system.items():
        print(f"{key}: {value}")

    print("\nDISK USAGE")
    disk = get_disk_usage("/")

    for key, value in disk.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
