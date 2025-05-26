import './globals.css';
import type { Metadata } from "next";
// Linhas de importação e definição das fontes Geist removidas

export const metadata: Metadata = {
  title: "Minha Aplicação",
  description: "Criado com Next.js",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="pt-BR">
      {/* Variáveis das fontes removidas da className */}
      <body
        className={`antialiased bg-gray-100 font-sans text-gray-900`}
      >
        {children}
      </body>
    </html>
  );
}
