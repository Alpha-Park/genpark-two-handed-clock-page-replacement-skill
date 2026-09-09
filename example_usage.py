from client import TwoHandedClock

def main():
    print("=== Testing Two-Handed Clock Algorithm ===")
    clock = TwoHandedClock(num_frames=4, hand_spread=2)
    clock.access_page("page_1")
    clock.access_page("page_2")
    clock.access_page("page_3")
    clock.access_page("page_4")

    # Access new page causing eviction
    res = clock.access_page("page_5")
    print("Page 5 Access Result:", res)
    assert res['status'] == 'FAULT'
    assert res['evicted'] is not None

    print("Two-Handed Clock verified successfully!")

if __name__ == '__main__':
    main()
