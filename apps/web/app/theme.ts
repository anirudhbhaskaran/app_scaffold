import { createTheme } from "@mui/material";


export const theme = createTheme({
  palette: {
    mode: 'light',
    primary: {
      main: '#185FA5',
    },
    secondary: {
      main: '#EF9F27',
    },
    background: {
      default: '#F1EFE8',
    },
    success: {
      main: '#008080',
    },
    warning: {
      main: '#FF7F50',
    },
    error: {
      main: '#800000',
    },
    info: {
      main: '#5e9db2',
    },
    text: {
      primary: '#000',
      secondary: '#737270',
      disabled: '#808080'
    },
  },
  typography: {
    fontFamily: `"Montserrat", "Roboto", "Helvetica", "Arial", sans-serif`,
  },
  shape: { borderRadius: 10 }
});
