import { create } from "zustand"
import { persist } from 'zustand/middleware'

type State = {
    access: string;
    refresh: string;
    is_auth: boolean;
}

type Actions = {
    setToken: (access: string, refresh: string) => void;
    logout: () => void;
};

export const useAuthStore = create(
    persist<State & Actions>(
        (set) => ({
            access: '',
            refresh: '',
            is_auth: false,
            setToken: (access: string, refresh: string) =>
                set(() => ({
                    access,
                    refresh,
                    is_auth: !!access && !!refresh,
                })),
                logout: () => set(() => ({ access: '', refresh: '', is_auth: false })), 
        }),
        {
            name: 'auth'
        }
    )
)