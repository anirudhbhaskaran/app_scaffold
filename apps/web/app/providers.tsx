// app/providers.tsx
"use client";

import { SessionProvider } from "next-auth/react";
import { CssBaseline, ThemeProvider } from '@mui/material';
import { theme } from "./theme";


export default function Providers({ children }: { children: React.ReactNode }) {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <SessionProvider>{children}</SessionProvider>
    </ThemeProvider>
  )
}