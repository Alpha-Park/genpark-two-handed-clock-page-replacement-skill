class TwoHandedClock:
    """BSD Two-Handed Clock Page Replacement Algorithm."""
    def __init__(self, num_frames, hand_spread=3):
        self.num_frames = num_frames
        self.hand_spread = hand_spread
        self.frames = [None] * num_frames
        self.ref_bits = [0] * num_frames
        self.age_hand = 0
        self.clear_hand = (self.age_hand + hand_spread) % num_frames

    def access_page(self, page_id):
        if page_id in self.frames:
            idx = self.frames.index(page_id)
            self.ref_bits[idx] = 1
            return {'status': 'HIT', 'frame': idx}

        victim_idx = None
        while victim_idx is None:
            self.ref_bits[self.clear_hand] = 0
            self.clear_hand = (self.clear_hand + 1) % self.num_frames

            if self.frames[self.age_hand] is None or self.ref_bits[self.age_hand] == 0:
                victim_idx = self.age_hand
                evicted = self.frames[victim_idx]
                self.frames[victim_idx] = page_id
                self.ref_bits[victim_idx] = 1
                self.age_hand = (self.age_hand + 1) % self.num_frames
                return {'status': 'FAULT', 'evicted': evicted, 'frame': victim_idx}

            self.age_hand = (self.age_hand + 1) % self.num_frames
