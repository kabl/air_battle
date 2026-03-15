import numpy as np
import pygame

SAMPLE_RATE = 44100


class SoundManager:

    def __init__(self):
        pygame.mixer.set_num_channels(16)

        self._simple_gun      = self._make_laser(900, 200, 0.12)
        self._double_gun      = self._make_laser(1200, 350, 0.10)
        self._missile_launch  = self._make_missile_launch(0.35)
        self._explosion       = self._make_explosion(0.55)
        self._player_hit      = self._make_player_hit(0.90)
        self._crash_explosion = self._make_crash_explosion(1.20)
        self._bg_music        = self._make_background_music()
        self._menu_music      = self._make_menu_music()

    # --- public API ---

    def play_simple_gun(self):
        self._simple_gun.play()

    def play_double_gun(self):
        self._double_gun.play()

    def play_missile_launch(self):
        self._missile_launch.play()

    def play_explosion(self):
        self._explosion.play()

    def play_player_hit(self):
        self._player_hit.play()

    def play_crash_explosion(self):
        self._crash_explosion.play()

    def start_music(self):
        self._bg_music.play(loops=-1)

    def stop_music(self):
        self._bg_music.stop()

    def start_menu_music(self):
        self._menu_music.play(loops=-1)

    def stop_menu_music(self):
        self._menu_music.stop()

    # --- sound generators ---

    @staticmethod
    def _to_sound(wave, volume=0.5):
        wave = np.clip(wave * volume, -1.0, 1.0)
        samples = (wave * 32767).astype(np.int16)
        stereo = np.ascontiguousarray(np.column_stack([samples, samples]))
        return pygame.sndarray.make_sound(stereo)

    def _make_laser(self, f_start, f_end, duration):
        n = int(SAMPLE_RATE * duration)
        freq = np.linspace(f_start, f_end, n)
        phase = np.cumsum(2 * np.pi * freq / SAMPLE_RATE)
        wave = np.sign(np.sin(phase))           # square wave — classic 8-bit laser
        env = np.linspace(1.0, 0.0, n) ** 0.5
        return self._to_sound(wave * env, volume=0.35)

    def _make_missile_launch(self, duration):
        n = int(SAMPLE_RATE * duration)
        freq = np.linspace(80, 450, n)
        phase = np.cumsum(2 * np.pi * freq / SAMPLE_RATE)
        tone = np.sin(phase)
        np.random.seed(42)
        noise = np.random.uniform(-1.0, 1.0, n)
        wave = tone * 0.65 + noise * 0.35
        attack = int(n * 0.08)
        env = np.concatenate([np.linspace(0, 1, attack),
                               np.linspace(1, 0.5, n - attack)])
        return self._to_sound(wave * env, volume=0.50)

    def _make_explosion(self, duration):
        n = int(SAMPLE_RATE * duration)
        t = np.arange(n) / SAMPLE_RATE
        np.random.seed(1)
        noise = np.random.uniform(-1.0, 1.0, n)
        freq = np.linspace(250, 40, n)
        phase = np.cumsum(2 * np.pi * freq / SAMPLE_RATE)
        tone = np.sin(phase)
        wave = noise * 0.55 + tone * 0.45
        env = np.exp(-t * 5.5)
        return self._to_sound(wave * env, volume=0.75)

    def _make_player_hit(self, duration):
        n = int(SAMPLE_RATE * duration)
        t = np.arange(n) / SAMPLE_RATE
        np.random.seed(2)
        noise = np.random.uniform(-1.0, 1.0, n)
        freq = np.linspace(380, 60, n)
        phase = np.cumsum(2 * np.pi * freq / SAMPLE_RATE)
        tone = np.sin(phase)
        wave = noise * 0.40 + tone * 0.60
        env = np.exp(-t * 2.8)
        return self._to_sound(wave * env, volume=0.85)

    def _make_crash_explosion(self, duration):
        n = int(SAMPLE_RATE * duration)
        t = np.arange(n) / SAMPLE_RATE

        # Layer 1 — sharp initial impact burst
        np.random.seed(7)
        impact = np.random.uniform(-1.0, 1.0, n)
        impact_env = np.exp(-t * 18)

        # Layer 2 — low rumble that lingers
        np.random.seed(8)
        rumble_noise = np.random.uniform(-1.0, 1.0, n)
        rumble_freq = np.linspace(180, 25, n)
        rumble_phase = np.cumsum(2 * np.pi * rumble_freq / SAMPLE_RATE)
        rumble = np.sin(rumble_phase) * 0.6 + rumble_noise * 0.4
        rumble_env = np.exp(-t * 3.5)

        # Layer 3 — mid crackle
        np.random.seed(9)
        crackle = np.random.uniform(-1.0, 1.0, n)
        crackle_env = np.exp(-t * 9) * np.sin(np.pi * t / (duration * 0.3)).clip(0)

        wave = impact * impact_env * 0.5 + rumble * rumble_env * 0.8 + crackle * crackle_env * 0.3
        return self._to_sound(wave, volume=0.90)

    def _make_menu_music(self):
        bpm = 165
        beat = 60.0 / bpm

        # A minor note map — aggressive, intense
        hz = {
            'A2': 110.00, 'E3': 164.81, 'A3': 220.00, 'B3': 246.94,
            'C4': 261.63, 'D4': 293.66, 'E4': 329.63, 'F4': 349.23,
            'G4': 392.00, 'A4': 440.00, 'B4': 493.88,
            'C5': 523.25, 'D5': 587.33, 'E5': 659.25, 'F5': 698.46,
            'G5': 783.99, 'A5': 880.00,
        }

        # Fast driving melody — A minor, aggressive
        melody = [
            ('A5', 0.25), ('G5', 0.25), ('F5', 0.25), ('E5', 0.25),
            ('D5', 0.25), ('C5', 0.25), ('D5', 0.25), ('E5', 0.25),
            ('A5', 0.5),  ('G5', 0.25), ('F5', 0.25),
            ('E5', 1.0),
            ('F5', 0.25), ('E5', 0.25), ('D5', 0.25), ('C5', 0.25),
            ('B4', 0.25), ('C5', 0.25), ('D5', 0.25), ('E5', 0.25),
            ('F5', 0.5),  ('E5', 0.25), ('D5', 0.25),
            ('A4', 1.0),
        ]

        # Power bass — root + fifth (Am - F - G - Am)
        bass = [
            ('A2', 1.0), ('E3', 1.0),
            ('A2', 1.0), ('E3', 1.0),
            ('F4', 1.0), ('C4', 1.0),  # F power chord approximation
            ('G4', 1.0), ('D4', 1.0),  # G power chord approximation
        ]

        def note_wave(freq, dur, shape):
            n = int(SAMPLE_RATE * dur)
            t = np.arange(n) / SAMPLE_RATE
            ph = 2 * np.pi * freq * t
            if shape == 'sawtooth':
                w = 2 * (t * freq - np.floor(t * freq + 0.5))
            elif shape == 'square':
                w = np.sign(np.sin(ph))
            else:  # triangle
                w = 2 * np.abs(2 * (t * freq - np.floor(t * freq + 0.5))) - 1
            atk = min(int(SAMPLE_RATE * 0.008), n)
            rel = min(int(SAMPLE_RATE * 0.04), n)
            env = np.ones(n)
            env[:atk] = np.linspace(0, 1, atk)
            env[n - rel:] = np.linspace(1, 0, rel)
            return w * env

        mel = np.concatenate([note_wave(hz[n], b * beat, 'square') * 0.32
                               for n, b in melody])
        bas = np.concatenate([note_wave(hz[n], b * beat, 'sawtooth') * 0.20
                               for n, b in bass])

        L = max(len(mel), len(bas))
        mel = np.pad(mel, (0, L - len(mel)))
        bas = np.pad(bas, (0, L - len(bas)))

        combined = np.clip(mel + bas, -1.0, 1.0)
        samples = (combined * 32767).astype(np.int16)
        stereo = np.ascontiguousarray(np.column_stack([samples, samples]))
        return pygame.sndarray.make_sound(stereo)

    def _make_background_music(self):
        bpm = 148
        beat = 60.0 / bpm

        # G major note map
        hz = {
            'G3': 196.00, 'A3': 220.00, 'B3': 246.94,
            'C4': 261.63, 'D4': 293.66, 'E4': 329.63, 'Fs4': 369.99, 'G4': 392.00,
            'A4': 440.00, 'B4': 493.88,
            'C5': 523.25, 'D5': 587.33, 'E5': 659.25, 'Fs5': 739.99, 'G5': 783.99,
            'A5': 880.00,
        }

        # Upbeat 8-bar arcade loop in G major
        melody = [
            ('G4', 0.5), ('B4', 0.5), ('D5', 0.5), ('B4', 0.5),
            ('G4', 0.5), ('A4', 0.5), ('B4', 1.0),
            ('C5', 0.5), ('E5', 0.5), ('G5', 0.5), ('E5', 0.5),
            ('C5', 0.5), ('D5', 0.5), ('E5', 1.0),
            ('D5', 0.5), ('Fs5', 0.5), ('A5', 0.5), ('Fs5', 0.5),
            ('D5', 0.5), ('E5', 0.5), ('Fs5', 1.0),
            ('G5', 0.5), ('Fs5', 0.5), ('E5', 0.5), ('D5', 0.5),
            ('C5', 0.5), ('B4', 0.5), ('G4', 1.0),
        ]

        bass = [
            ('G3', 2.0), ('D4', 2.0),
            ('C4', 2.0), ('G3', 2.0),
            ('D4', 2.0), ('A3', 2.0),
            ('G3', 2.0), ('G3', 2.0),
        ]

        def note_wave(freq, dur, shape):
            n = int(SAMPLE_RATE * dur)
            t = np.arange(n) / SAMPLE_RATE
            ph = 2 * np.pi * freq * t
            if shape == 'square':
                w = np.sign(np.sin(ph))
            else:  # triangle
                w = 2 * np.abs(2 * (t * freq - np.floor(t * freq + 0.5))) - 1
            atk = min(int(SAMPLE_RATE * 0.012), n)
            rel = min(int(SAMPLE_RATE * 0.05), n)
            env = np.ones(n)
            env[:atk] = np.linspace(0, 1, atk)
            env[n - rel:] = np.linspace(1, 0, rel)
            return w * env

        mel = np.concatenate([note_wave(hz[n], b * beat, 'square') * 0.30
                               for n, b in melody])
        bas = np.concatenate([note_wave(hz[n], b * beat, 'triangle') * 0.22
                               for n, b in bass])

        L = max(len(mel), len(bas))
        mel = np.pad(mel, (0, L - len(mel)))
        bas = np.pad(bas, (0, L - len(bas)))

        combined = np.clip(mel + bas, -1.0, 1.0)
        samples = (combined * 32767).astype(np.int16)
        stereo = np.ascontiguousarray(np.column_stack([samples, samples]))
        return pygame.sndarray.make_sound(stereo)
