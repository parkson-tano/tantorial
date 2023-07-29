import React, { useState, useEffect } from "react";
import {
  TextInput,
  PasswordInput,
  Checkbox,
  Anchor,
  Paper,
  Title,
  Text,
  Container,
  Group,
  Button,
  Select,
} from "@mantine/core";
import { IconChevronDown } from "@tabler/icons-react";
import SignupHead from "../../components/SignupHead";

export default function StudentRegister() {
  const [searchValue, onSearchChange] = useState("");
  const [classValue, onClassChange] = useState("");
  return (
    <div
      style={{
        backgroundImage: `url(https://app.gradely.co/auth/img/AuthBg.0d514f33.svg)`,
      }}
    >
      <Container size={520} my={40}>
        <SignupHead title="Student" />
        <Paper withBorder shadow="md" p={30} mt={30} radius="md">
          <TextInput label="First Name" required />
          <TextInput label="Last Name" required />
          <Select
            mt="md"
            label="Subsystem"
            data={['English', 'French', 'Bilingual']}
            rightSection={<IconChevronDown size="1rem" />}
            placeholder="Select Subsystem"
          />
          <Select
            mt="md"
            label="Your School"
            searchable
            onSearchChange={onSearchChange}
            searchValue={searchValue}
            rightSection={<IconChevronDown size="1rem" />}
            nothingFound="Your School is not listed"
            data={["React", "Angular", "Svelte", "Vue"]}
          />
          <Select
            mt="md"
            label="Your Class"
            searchable
            onSearchChange={onClassChange}
            searchValue={classValue}
            rightSection={<IconChevronDown size="1rem" />}
            nothingFound="Your Class is not listed"
            data={["React", "Angular", "Svelte", "Vue"]}
          />

          {/* <TextInput
          type="number"
          label="Phone Number"
            icon={<Text color="gray" ml="xr"> +237</Text>}
          required
        />
        <TextInput
          label="Email"
          placeholder="you@mantine.dev"

          required /> */}
          <PasswordInput
            label="Password"

            required
            mt="md"
          />
          <PasswordInput
            label="Confirm Password"

            required
            mt="md"
          />
          <Button
            fullWidth
            mt="xl"
            style={{
              backgroundColor: "#FFC107",
            }}
          >
            Sign in
          </Button>
        </Paper>
      </Container>
    </div>
  );
}
