import { render, screen, fireEvent } from "@testing-library/react";
import App from "./App";

describe("App Component", () => {
  it("renders the initial UI elements correctly", () => {
    render(<App />);

    // Check if the heading is rendered
    expect(screen.getByText("Vite + React")).toBeInTheDocument();

    // Check if the counter button is rendered with initial count
    expect(screen.getByText("count is 0")).toBeInTheDocument();

    // Check if the logos are rendered
    expect(screen.getByAltText("Vite logo")).toBeInTheDocument();
    expect(screen.getByAltText("React logo")).toBeInTheDocument();

    // Check if the instruction text is rendered by looking for the code element
    expect(screen.getByText("src/App.tsx")).toBeInTheDocument();
  });

  it("increments counter when button is clicked", () => {
    render(<App />);

    // Find the counter button
    const counterButton = screen.getByText("count is 0");

    // Click the button once
    fireEvent.click(counterButton);
    expect(screen.getByText("count is 1")).toBeInTheDocument();

    // Click the button again
    fireEvent.click(counterButton);
    expect(screen.getByText("count is 2")).toBeInTheDocument();

    // Click the button multiple times
    fireEvent.click(counterButton);
    fireEvent.click(counterButton);
    fireEvent.click(counterButton);
    expect(screen.getByText("count is 5")).toBeInTheDocument();
  });
});
