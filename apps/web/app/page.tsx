// app/page.tsx

import { getServerSession } from "next-auth";
import { authOptions } from "@/app/api/auth/[...nextauth]/route";
import { redirect } from "next/navigation";

export default async function Home() {
  const session = await getServerSession(authOptions);

  // Not logged in → go to Keycloak
  if (!session) {
    redirect("/api/auth/signin/keycloak");
  }

  // Logged in → go to home
  redirect("/home");
}