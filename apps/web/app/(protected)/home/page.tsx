'use client';

import { useSession } from "next-auth/react";

export default function HomePage() {
  const { data: session } = useSession();

  return (
    <>Hi {session?.user?.name}</>
  );
}