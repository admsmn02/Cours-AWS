import { render, screen, fireEvent } from "@testing-library/react";
import App from "./App";

describe("App Component", () => {
  it("renders the main heading and initial counter", () => {
    render(<App />);

    // Check if the main heading is rendered
    expect(
      screen.getByRole("heading", { name: "Vite + React" })
    ).toBeInTheDocument();

    // Check if the counter button is rendered with initial count
    expect(
      screen.getByRole("button", { name: "count is 0" })
    ).toBeInTheDocument();

    // Check if the logos are rendered
    expect(screen.getByAltText("Vite logo")).toBeInTheDocument();
    expect(screen.getByAltText("React logo")).toBeInTheDocument();
  });

  it("increments counter when button is clicked multiple times", () => {
    render(<App />);

    // Find the counter button
    const counterButton = screen.getByRole("button", { name: "count is 0" });

    // Click the button once
    fireEvent.click(counterButton);
    expect(
      screen.getByRole("button", { name: "count is 1" })
    ).toBeInTheDocument();

    // Click the button again
    fireEvent.click(counterButton);
    expect(
      screen.getByRole("button", { name: "count is 2" })
    ).toBeInTheDocument();

    // Click the button multiple times
    fireEvent.click(counterButton);
    fireEvent.click(counterButton);
    fireEvent.click(counterButton);
    expect(
      screen.getByRole("button", { name: "count is 5" })
    ).toBeInTheDocument();
  });
});
