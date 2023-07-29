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
import { IconAt } from "@tabler/icons-react";
import { IconChevronDown } from "@tabler/icons-react";
import SignupHead from "../../components/SignupHead";

export default function SchoolRegister() {
  const [searchValue, onSearchChange] = useState("");
  const [classValue, onClassChange] = useState("");
  const [schoolTeacher, setSchoolTeacher] = useState(false);
  return (
    <div
      style={{
        backgroundImage: `url(https://app.gradely.co/auth/img/AuthBg.0d514f33.svg)`,
      }}
    >
      <Container size={520} my={40}>
        <SignupHead title="School" />

        <Paper withBorder shadow="md" p={30} mt={30} radius="md">
          <TextInput label="Full Name"
            my="md"
            required />
          <TextInput label="School Name"
            my="md"
            required />
          <TextInput
            type="number"
            label="Phone Number"
            my="md"
            icon={<Text color="gray" ml="xr"> +237</Text>}
            required
          />
          <TextInput
            label="Email"
            placeholder="you@mantine.dev"
            icon={<IconAt size="0.8rem" />}
            required />
          <PasswordInput
            label="Password"
            my="md"
            required
            mt="md"
          />
          <PasswordInput
            label="Confirm Password"
            my="md"
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
