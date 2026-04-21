import { getSession } from "next-auth/react";

const session = await getSession();

const res = await fetch("http://localhost:8000/api", {
  headers: {
    Authorization: `Bearer ${session?.accessToken}`,
  },
});